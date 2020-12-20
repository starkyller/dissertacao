
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>
    <h2 style="display: inline-block">Table of Contents</h2>
  </summary>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#build-with">Built With</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
        <a href="#usage">Usage</a>
    </li>
</details>





<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Build With

* [Django](https://github.com/django/django)

### Prerequisites

This is an example of how to list things you need to use the software.
* Python 3.6.9+
* [pipenv](https://pypi.org/project/pipenv/)


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/starkyller/dissertacao.git
   ```
2. Change Directory to backend
   ```sh
   cd backend
   ```
3. Install dependencies
   ```sh
   pipenv install --dev
   ```
4. Generate SQLite Database
    ```sh
   ./hmobiweb/manage.py migrate
   ```
5. Create a superuser
    ```sh
   ./hmobiweb/manage.py createsuperuser
   ```
6. Run the local server
    ```sh
   ./hmobiweb/manage.py runserver
   ```
7. Navigate to /admin on a browser and have fun

<!-- USAGE EXAMPLES -->
## Usage

To be written

<!--_For more examples, please refer to the [Documentation]()_ -->


