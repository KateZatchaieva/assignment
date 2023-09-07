## How to run

#### Docker
To run automation in Docker:
1. `docker build -t qbtech_assign . `
2.  `docker run  -v $(pwd)/report:/automation/jsonplaceholder_assignment/report qbtech_assign`

Report will be generated in /report directory, under your working directory

#### Local
To run automation locally:
1. Install latest python
2. Open project directory and run next command from /qbtech_assignment directory:
   `pip3 install -r requirements.txt`
3. Run tests:
    `pytest --html=report/report.html`

