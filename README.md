# zrh-waiting-time

Scraping and presenting tool for Zürich airport security check waiting times

## Scraping

The scraped endpoint is:

```shell
curl https://dxp-fds.flughafen-zuerich.ch/WaitingTimes
```

Response example:

```json
{
  "maxWaitingTime": "1-3"
}
```
