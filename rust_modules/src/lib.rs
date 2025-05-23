use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use rustii::archive::lz77;


#[pyfunction]
fn rs_compress_lz77(py: Python<'_>, data: &[u8]) -> PyResult<Vec<u8>> {
    py.allow_threads(|| {
        Ok(lz77::compress_lz77(data).unwrap())
    })
}

#[pyfunction]
fn rs_decompress_lz77(py: Python<'_>, data: &[u8]) -> PyResult<Vec<u8>> {
    py.allow_threads(|| {
        match lz77::decompress_lz77(data) {
            Ok(r) => Ok(r),
            Err(e) => Err(PyValueError::new_err(e.to_string())),
        }
    })
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_modules(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rs_compress_lz77, m)?)?;
    m.add_function(wrap_pyfunction!(rs_decompress_lz77, m)?)?;
    Ok(())
}
