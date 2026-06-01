
## SETUP.md

```markdown
# Setup Guide

## Step 1: Get Twitter API Keys

1. Go to https://developer.twitter.com/
2. Sign in with your Twitter account
3. Click "Developer Portal"
4. Create a new app
5. Generate OAuth 1.0 credentials

You will get:
- Consumer Key
- Consumer Secret
- Access Token
- Access Token Secret

## Step 2: Create Config File

Create `twitter_config.json`:

```json
{
    "consumer_key": "YOUR_CONSUMER_KEY",
    "consumer_secret": "YOUR_CONSUMER_SECRET",
    "access_token": "YOUR_ACCESS_TOKEN",
    "access_token_secret": "YOUR_ACCESS_TOKEN_SECRET"
}
make proxies.txt
and add your proxies there
