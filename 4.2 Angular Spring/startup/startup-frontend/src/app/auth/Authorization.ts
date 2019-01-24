export class Authorization {
  groups: String[];
  roles: String[];

  constructor(json: any) {
    this.groups = json.authorization.groups;
    this.roles = json.authorization.roles;
  }
}
