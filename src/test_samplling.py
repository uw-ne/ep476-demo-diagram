import pytest
import numpy as np

import sampling as smp


def test_isotropic_coord_x():

    inputs = (0.5,0)
    expected_dir = np.array([1,0,0])
    observed_dir = smp.isotropic_direction(inputs)

    assert expected_dir == pytest.approx(observed_dir)

def test_isotropic_coord_y():

    inputs = (0.5,0.25)
    expected_dir = np.array([0,1,0])
    observed_dir = smp.isotropic_direction(inputs)

    assert expected_dir == pytest.approx(observed_dir)
    
def test_isotropic_coord_z():

    inputs = (0,0)
    expected_dir = np.array([0,0,1])
    observed_dir = smp.isotropic_direction(inputs)

    assert expected_dir == pytest.approx(observed_dir)

def test_isotropic_110():

    inputs = (0.5,0.125)
    expected_dir = np.array([1,1,0])/np.sqrt(2)
    observed_dir = smp.isotropic_direction(inputs)

    assert expected_dir == pytest.approx(observed_dir)

def test_isotropic_101():

    inputs = (0.1464466094,0)
    expected_dir = np.array([1,0,1])/np.sqrt(2)
    observed_dir = smp.isotropic_direction(inputs)

    assert expected_dir == pytest.approx(observed_dir)

def test_isotropic_011():

    inputs = (0.1464466094,0.25)
    expected_dir = np.array([0,1,1])/np.sqrt(2)
    observed_dir = smp.isotropic_direction(inputs)

    assert expected_dir == pytest.approx(observed_dir)

def test_isotropic_011():

    inputs = (0.211324865,0.125)
    expected_dir = np.array([1,1,1])/np.sqrt(3)
    observed_dir = smp.isotropic_direction(inputs)

    assert expected_dir == pytest.approx(observed_dir)


