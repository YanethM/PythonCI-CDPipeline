import sys
import os
import pytest
import json
from unittest.mock import patch, mock_open

# Añadir el directorio 'src' al sys.path para que Python pueda encontrar 'problematic_code'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importar el código que vamos a probar
from problematic_code import (
    authenticate_user,
    read_user_file,
    add_user,
    calculate_fibonacci,
    unsafe_system_call,
    complex_logic,
)

# Prueba para authenticate_user
def test_authenticate_user():
    assert authenticate_user("admin", "admin123") == True  # Credenciales correctas
    assert authenticate_user("admin", "wrong_password") == False  # Contraseña incorrecta
    assert authenticate_user("user", "admin123") == False  # Usuario incorrecto

# Prueba para read_user_file
@patch("builtins.open", new_callable=mock_open, read_data='{"user1": "pass1"}')
def test_read_user_file(mock_file):
    data = read_user_file("dummy.json")
    assert data == {"user1": "pass1"}
    mock_file.assert_called_once_with("dummy.json", "r")

# Prueba para add_user
@patch("builtins.open", new_callable=mock_open)
@patch("problematic_code.read_user_file", return_value={"user1": "pass1"})
def test_add_user(mock_read_user_file, mock_open_file):
    add_user("dummy.json", "user2", "pass2")
    mock_read_user_file.assert_called_once_with("dummy.json")
    mock_open_file.assert_called_once_with("dummy.json", "w")
    
    # Combina las llamadas a `write` en una sola cadena para verificar el resultado final
    written_data = "".join(call.args[0] for call in mock_open_file().write.call_args_list)
    assert json.loads(written_data) == {"user1": "pass1", "user2": "pass2"}

# Prueba para calculate_fibonacci
@pytest.mark.parametrize("input,expected", [(0, 0), (1, 1), (5, 5), (10, 55)])
def test_calculate_fibonacci(input, expected):
    assert calculate_fibonacci(input) == expected

# Prueba para unsafe_system_call
@patch("os.system")
def test_unsafe_system_call(mock_os_system):
    unsafe_system_call("ls")
    mock_os_system.assert_called_once_with("ls")

# Prueba para complex_logic
@patch("builtins.print")
def test_complex_logic(mock_print):
    # Caso con "key2"
    data = {"key1": "value1", "key2": "value2", "key4": "value4"}
    complex_logic(data)
    mock_print.assert_any_call("value2")

    # Caso sin "key3"
    data = {"key1": "value1", "key3": "value3"}
    complex_logic(data)
    mock_print.assert_any_call("Missing key3")

    # Caso sin "key4"
    data = {"key1": "value1"}
    complex_logic(data)
    mock_print.assert_any_call("No key4")