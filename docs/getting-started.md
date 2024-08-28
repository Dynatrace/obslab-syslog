You will need to collect some information before you can begin.

## Prerequisites
- A Dynatrace tenant ([sign up for a free trial](https://dt-url.net/trial){target=_blank})
- A Dynatrace API token with `logs.ingest` permissions (see below)

## Format URL

Make a note of your Dynatrace tenant ID. It is the first bit of your URL (eg. abc12345 in the following examples):

```
https://abc12345.live.dynatrace.com
https://abc12345.apps.dynatrace.com
```

Reformat the URL like this: `https://TENANT_ID.live.dynatrace.com`

eg. `https://abc12345.live.dynatrace.com`

## Create API Token
In Dynatrace:

* Press `ctrl + k` and search for `access tokens`
* Create a new access token with the `logs.ingest` permission

You have all the necessary details and are ready to get started.

## [>> Click here to continue](start-demo.md)