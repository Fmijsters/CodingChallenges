interface AuthConfig {
  clientID: string;
  domain: string;
  callbackURL: string;
}

export const AUTH_CONFIG: AuthConfig = {
  clientID: 'XMYfyI76PIWDBQBTsFsNY4gzosIj44xg',
  domain: 'minor.eu.auth0.com',
  callbackURL: 'http://localhost:4200/callback'
};
