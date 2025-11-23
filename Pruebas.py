import pytest
from original import (
    construir_grafo_libro_libro,
    construir_grafo_libro,
    dijkstra,
    reconstruir
)

def test_construir_grafo_libro_libro():
    datos = {
        "L1": {"usuarios": [1, 2, 3]},
        "L2": {"usuarios": [2, 3]},
        "L3": {"usuarios": [4]}
    }

    grafo = construir_grafo_libro_libro(datos, m_minimo=2)

    assert "L1" in grafo
    assert "L2" in grafo
    assert grafo["L1"]["L2"] == pytest.approx(1 / (1 + 2))
    assert "L3" not in grafo["L1"]


def test_construir_grafo_libro():
    datos = {
        "U1": ["A", "B"],
        "U2": ["A", "B", "C"],
        "U3": ["X"]
    }

    grafo = construir_grafo_libro(datos, m_minimo=2)

    assert "U1" in grafo
    assert grafo["U1"]["U2"] == pytest.approx(1 / (1 + 2))
    assert "U3" not in grafo["U1"]


def test_dijkstra_simple():
    grafo = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2},
        "C": {"A": 4, "B": 2}
    }

    dist, prev = dijkstra(grafo, "A")

    assert dist["C"] == 3  # ruta A → B → C
    assert prev["C"] == "B"
    assert prev["B"] == "A"


def test_reconstruir():
    previo = {
        "A": None,
        "B": "A",
        "C": "B"
    }

    camino = reconstruir(previo, "C")
    assert camino == ["A", "B", "C"]
