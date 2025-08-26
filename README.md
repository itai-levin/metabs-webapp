# metabs-webapp
Webapp to display predicted spectral data for metabolites

For simple deployment: 
- `unzip -j data/webapp-data.zip -d data`
- `streamlit run Home.py`


To deploy a website that can be accessed with https :
- Obtain SSL certificates for your server using [certbot](https://certbot.eff.org/instructions?ws=nginx&os=pip): `certbot --nginx -d <SERVER NAME>`
- Deploy with Docker:
	- `docker compose up -d`
