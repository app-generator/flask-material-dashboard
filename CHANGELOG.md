# Change Log

## [1.0.7] 2022-05-30
### Improvements

- Built with [Material Dashboard Generator](https://appseed.us/generator/material-dashboard/)
  - Timestamp: `2022-05-30 21:22`

## [1.0.6] 2022-01-16
### Improvements

- Bump Flask Codebase to [v2stable.0.1](https://github.com/app-generator/boilerplate-code-flask-dashboard/releases)
- Dependencies update (all packages) 
  - Flask==2.0.2 (latest stable version)
  - flask_wtf==1.0.0
  - jinja2==3.0.3
  - flask-restx==0.5.1
- Forms Update:
  - Replace `TextField` (deprecated) with `StringField`

## Unreleased
### Fixes

- 2021-11-08 - `v1.0.6-rc1`
  - ImportError: [cannot import name 'TextField' from 'wtforms'](https://docs.appseed.us/content/how-to-fix/cannot-import-name-textfield-from-wtforms)
    - Problem caused by `WTForms-3.0.0`
    - Fix: use **WTForms==2.3.3**
    
## [1.0.5] 2021-10-22
### Improvements

- Bump UI: Material Dashboard - v3.0.0
  - Update Bootstrap to v5.1.3
  - Update to Material Design 2
- Bump Codebase: [Flask Dashboard](https://github.com/app-generator/boilerplate-code-flask-dashboard) v2.0.0
  - Dependencies update (all packages) 
    - Flask==2.0.1 (latest stable version)
  - Better Code formatting
  - Improved Files organization
  - Optimize imports
  - Docker Scripts Update
  - Gulp Tooling  (SASS Compilation)

## [1.0.4] 2021-05-16
### Dependencies Update

- Bump Codebase: [Flask Dashboard](https://github.com/app-generator/boilerplate-code-flask-dashboard) v1.0.6
- Freeze used versions in `requirements.txt`
    - jinja2 = 2.11.3
    
## [1.0.3] 2021-03-18
### Improvements

- Bump Codebase: [Flask Dashboard](https://github.com/app-generator/boilerplate-code-flask-dashboard) v1.0.5
- Freeze used versions in `requirements.txt`
    - flask_sqlalchemy = 2.4.4
    - sqlalchemy = 1.3.23
    
## [1.0.2] 2021-01-13
### Improvements & Bug Fixes

- 2021-01-13 - Improvements
   - Bump UI: [Jinja Material](https://github.com/app-generator/jinja-material-dashboard) v1.0.2
   - Bump Codebase: [Flask Dashboard](https://github.com/app-generator/boilerplate-code-flask-dashboard) v1.0.3 

- 2020-09-11 - Improvements
    - Codebase & UI Update
    - Update sidebar item based on selected page

## [1.0.1] 2020-07-12
### Improvements

- Codebase update: [Flask Dashboard Boilerplate](https://github.com/app-generator/boilerplate-code-flask-dashboard) v1.0.1

## [1.0.0] 2019-07-19
### Initial Release
