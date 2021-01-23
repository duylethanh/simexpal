
import os
import pytest

from simexpal import util

file_dir = os.path.abspath(os.path.dirname(__file__))
valid_experiments_ymls = ['../../examples/sorting/',
                          '../../examples/sorting_cpp/',
                          '../../examples/download_instances/']

invalid_experiments_ymls = ['invalid_ymls/top_level-additional_property.yml',
                            'invalid_ymls/repo-invalid_value.yml']

@pytest.mark.parametrize('rel_yml_path', valid_experiments_ymls)
def test_valid_experiments_yml(rel_yml_path):
    yml_dir = os.path.join(file_dir, rel_yml_path)
    util.try_rmfile(os.path.join(yml_dir, 'validation.cache'))  # Make sure that caches from previous calls are deleted.
    ret_val = util.validate_setup_file(yml_dir, 'experiments.yml', 'experiments.json')

    assert isinstance(ret_val, dict)

@pytest.mark.parametrize('rel_yml_path', invalid_experiments_ymls)
def test_invalid_experiments_yml(rel_yml_path):
    rel_yml_dir = os.path.dirname(rel_yml_path)
    yml_dir = os.path.join(file_dir, rel_yml_dir)
    filename = os.path.basename(rel_yml_path)

    with pytest.raises(SystemExit) as info:
        util.validate_setup_file(yml_dir, filename, 'experiments.json')

    assert info.value.code == 1
