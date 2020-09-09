To run the MLflow Tracking UI on local:       
`mlflow ui`

On server:

Bash-> env/bin/mlflow ui --host $(hostname -f)

Then it outputs a url with http:// at the begininig.

Remove the http (keep the ip and port)

Put the ip and port in a local terminal in the following format:

Local bash-> ssh -L :: username@cluster.servername