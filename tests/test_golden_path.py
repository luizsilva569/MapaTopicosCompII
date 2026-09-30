from src.controls import authorize_access, feature_flag


def test_golden_path_smoke_critical_flow() -> None:
    """Smoke test for the golden path and critical journey."""
    assert authorize_access("operator", "read") is True


def test_negative_authorization_forbidden_invariant_regression() -> None:
    """Negative regression test protects the authorization invariant constraint."""
    forbidden = authorize_access("", "privileged")
    assert forbidden is False


def test_safe_change_feature_flag() -> None:
    assert feature_flag("candidate", True) is True
