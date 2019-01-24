import {Authorization} from './Authorization';

export class User {
  sub: String;
  nickname: String;
  name: String;
  picture: String;
  updated_at: Date;
  authorization: Authorization;
  json: String;

  constructor(json: any) {
    this.sub = json.sub;
    this.nickname = json.nickname;
    this.name = json.name;
    this.picture = json.picture;
    this.updated_at = json.updated_at;
    this.authorization = new Authorization(json['https://minor:eu:auth0:com/app_metadata']);
    this.json = json;
  }
}
