import {Component, OnInit, Optional, SkipSelf} from '@angular/core';
import {AuthService} from '../auth/auth.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  profile: any;

  constructor(@Optional() @SkipSelf() public auth: AuthService) {
    this.auth.routingAdress = 'profile';
  }

  ngOnInit() {
    if (this.auth.isAuthenticated()) {
      if (this.auth.userProfile) {
        console.log('1');
        this.profile = this.auth.userProfile;
      } else {
        console.log('2');
        this.auth.getProfile((err, profile) => {
          this.profile = profile;
        });
      }
    } else {
      this.auth.login();
    }
  }

}
