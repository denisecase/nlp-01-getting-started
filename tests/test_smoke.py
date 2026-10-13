"""Offline smoke test for web acquisition and token frequency analysis."""

import runpy
from types import SimpleNamespace

import matplotlib.pyplot as plt
import requests


def test_web_words_counts_sample_html(monkeypatch, tmp_path):
    """Run the example without HTTP access or interactive chart windows."""
    html = "<html><body><p>Language language language. Data data.</p></body></html>"
    requested_urls = []

    def fake_get(url, *, headers, timeout):
        requested_urls.append(url)
        assert "User-Agent" in headers
        assert timeout == 30
        return SimpleNamespace(text=html, raise_for_status=lambda: None)

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(requests, "get", fake_get)
    monkeypatch.setattr(plt, "show", lambda: plt.close("all"))

    result = runpy.run_module("nlp.web_words", run_name="__main__")

    assert len(requested_urls) == 1
    assert result["freq_dict"]["language"] == 3
    assert result["freq_dict"]["data"] == 2
    assert sum(result["freq_dict"].values()) == len(result["clean_words"])
