# lti-mikrotik-python

> ⚠️ **Warning**: This project is an **academic project** and is intended for educational purposes only. It may not cover all edge cases or advanced Mikrotik configurations.

This project is a Python-based middleware for managing Mikrotik routers. It provides a RESTful API to interact with Mikrotik devices, enabling functionalities such as interface management, peer configuration, and network monitoring. It is designed to work seamlessly with the [lti-mikrotik](https://github.com/iuricarras/lti-mikrotik) Vue.js-based frontend.

## Main Functionalities

- **Manage Multiple Devices**: Control more than one Mikrotik device using the same backend.
- **Interface Management**:
  - List all interfaces of the device.
  - List only wireless interfaces.
- **Bridge Management**:
  - List, create, edit, and delete bridge interfaces and their associated ports.
- **Wireless Security Profiles**:
  - Create, edit, and delete security profiles for use in wireless networks.
- **Wireless Network Management**:
  - Enable, disable, and configure wireless networks.
- **Static Routes**:
  - List, create, edit, and delete static routes.
- **IP Address Management**:
  - List, create, edit, and delete IP addresses.
- **DHCP Servers**:
  - List, create, edit, and delete DHCP servers.
- **DNS Server Management**:
  - Enable, disable, and configure the DNS server.
- **WireGuard Management**:
  - Manage WireGuard interfaces and peers.

## Project Setup

Follow these steps to set up the backend:

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- SQLite (or any other database supported by SQLAlchemy)

### Installation

#### Using Virtual Environment

1. Clone the repository:
   ```sh
   git clone https://github.com/iuricarras/lti-mikrotik-python.git
   cd lti-mikrotik-python
   ```

2. Set up a virtual environment:  
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables: Create a .env file in the root directory and add the following: 
    ```sh
    SECRETKEY=<your_secret_key>
    ```
The secret key needs to be a 32 bytes base64 string. You can generate a random string using the `openssl` command:
    ```
    openssl rand -base64 32
    ```


#### Using Nix Shell

1. Clone the repository:
   ```sh
   git clone https://github.com/iuricarras/lti-mikrotik-python.git
   cd lti-mikrotik-python
   ```

2. Enter the Nix shell: 
    ```sh
    nix-shell
    ```

3. Set up the environment variables: Create a .env file in the root directory and add the following: 
    ```sh
    SECRETKEY=<your_secret_key>
    ```
The secret key needs to be a 32 bytes base64 string. You can generate a random string using the `openssl` command:
    ```
    openssl rand -base64 32
    ```




### Running the Project
To start the Flask development server:
```sh
export FLASK_APP=project
export FLASK_DEBUG=1
flask run
```
The server will be available at `http://127.0.0.1:5000`.

### Deployment
For production, use a WSGI server like Gunicorn or uWSGI. Example with Gunicorn:
```sh
gunicorn -w 4 -b 0.0.0.0:5000 "project:create_app()"
```

## Notes
This project is intended for academic purposes and may not cover all edge cases or advanced Mikrotik configurations. Use it as a learning tool or as a starting point for more complex projects.

## License
This project is licensed under the MIT License. See the LICENSE file for more details. 
