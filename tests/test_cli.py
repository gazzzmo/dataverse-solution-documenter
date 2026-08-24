"""
Tests for CLI interface (dsd).
"""
import zipfile
import pytest
from pathlib import Path
from app.cli import main, create_parser


@pytest.fixture
def sample_zip(tmp_path):
    zip_path = tmp_path / "test_solution.zip"
    solution_xml = b"""<?xml version="1.0" encoding="utf-8"?>
<ImportExportXml>
  <SolutionManifest>
    <UniqueName>TestCliSolution</UniqueName>
    <LocalizedNames>
      <LocalizedName description="Test CLI Solution" languagecode="1033" />
    </LocalizedNames>
    <Descriptions>
      <Description description="A test solution" languagecode="1033" />
    </Descriptions>
    <Version>1.0.0.0</Version>
    <Managed>0</Managed>
    <Publisher>
      <UniqueName>TestPub</UniqueName>
      <LocalizedNames>
        <LocalizedName description="Test Publisher" languagecode="1033" />
      </LocalizedNames>
      <CustomizationPrefix>ts</CustomizationPrefix>
      <CustomizationOptionValuePrefix>10000</CustomizationOptionValuePrefix>
    </Publisher>
    <RootComponents />
  </SolutionManifest>
</ImportExportXml>"""

    customizations_xml = b"""<?xml version="1.0" encoding="utf-8"?>
<ImportExportXml>
  <Entities />
  <Roles />
  <Workflows />
  <optionsets />
</ImportExportXml>"""

    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.writestr("solution.xml", solution_xml)
        zf.writestr("customizations.xml", customizations_xml)

    return zip_path


def test_cli_parser_required_args():
    parser = create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([])


def test_cli_missing_input(tmp_path):
    output_dir = tmp_path / "out"
    missing_zip = tmp_path / "non_existent.zip"
    exit_code = main(["-i", str(missing_zip), "-o", str(output_dir)])
    assert exit_code == 1


def test_cli_invalid_extension(tmp_path):
    output_dir = tmp_path / "out"
    txt_file = tmp_path / "file.txt"
    txt_file.write_text("not a zip")
    exit_code = main(["-i", str(txt_file), "-o", str(output_dir)])
    assert exit_code == 1


def test_cli_success(sample_zip, tmp_path):
    output_dir = tmp_path / "out"
    exit_code = main(["-i", str(sample_zip), "-o", str(output_dir), "-v"])
    assert exit_code == 0
    assert output_dir.exists()
    assert (output_dir / "README.md").exists()
    assert (output_dir / "solution-overview.md").exists()
