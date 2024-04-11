#!/usr/bin/env python3
# serve.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            try:
                # Execute the command to get the output of script.py using sudo
                output_script1 = subprocess.check_output(["sudo", "python3", "script.py"], universal_newlines=True)
                # Execute the command to get the output of another_script.py using sudo
                output_script2 = subprocess.check_output(["sudo", "python3", "diagnosis.py"], universal_newlines=True)
                # Send the HTML template with the output embedded
                self.wfile.write(self.create_html(output_script1, output_script2).encode('utf-8'))
            except subprocess.CalledProcessError as e:
                self.wfile.write(f"Error: {e}".encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 - Not Found')

    def create_html(self, output_script1, output_script2):
        # Define the HTML template with the provided styles and script outputs
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Live Data - rbrinto</title>
            <style>
                body {{
                    background-color:  #010101; /* #1b33aa; Very dark green background */
                    color: #ffffff; /* White text */
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 80%;
                    max-width: 600px;
                    margin: 50px auto;
                    padding: 20px;
                    background-color: #1a511a; /* Dark green box background */
                    box-shadow: 0 8px 16px rgba(72, 227, 20, 1.0); /* Box shadow */
                    transition: box-shadow 0.6s;
                    overflow: auto; /* Enable scrolling if content exceeds container */
                }}
                .container:hover {{
                    box-shadow: 0 100px 128px rgba(152, 190, 35, 1.0); /* Box shadow on hover */
                }}
                #output1, #output2 {{
                    max-height: 300px; /* Set maximum height for output */
                    overflow-y: auto; /* Enable vertical scrolling if output exceeds container */
                    margin-top: 20px; /* Add margin between boxes */
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Vehicle Realtime IOT Monitoring</h1>
                <pre id="output1">{output_script1}</pre>
            </div>
            <div class="container">
                <h1>Vehicle Diagnosis</h1>
                <pre id="output2">{output_script2}</pre>
            </div>

            <script>
                // No JavaScript needed for this example
            </script>
        </body>
        </html>
        """
        return html_template

def run_server():
    server_address = ('', 80)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server is running...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
