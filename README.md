# noiip_updater
Simple Python script to do a single update for No-IP DDNS site.

Usage:

The first step is to set the authentication related entries:

* user_id: base64 encoded username
* auth_key: base64 encoded password
* hostname: name of the DDNS host (eg. raspberrypiezeero.ddns.net)
* headers: must be set correctly to allow the client to update the DDNS host. Example could be found in the code.

The IP will be updated on each execution, therefore it is recommended to execute it manually eg. in every fifth minute. Debug prints are enabled by default (TBH: there are no other prints :) ) and it is highly recommended to save them somehow.

crontab entry to do that:
*/5 *   * * *   root    python /opt/noip-updater.py >> /var/log/noip-updater.log
