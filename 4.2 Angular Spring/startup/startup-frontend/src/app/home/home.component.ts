import {Component, OnInit, Optional, SkipSelf} from '@angular/core';
import {AuthService} from '../auth/auth.service';
import {HomeControllerService} from '../../generated/api-client';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(@Optional() @SkipSelf() public auth: AuthService, apiclient: HomeControllerService) {
    if (this.auth.isAuthenticated()) {
      apiclient.configuration.accessToken = auth.idToken;
      apiclient.configuration.withCredentials = false;
      apiclient.defaultHeaders.set('Authorization', auth.idToken);
      console.log(apiclient.defaultHeaders.keys());
      apiclient.getTextUsingGET().subscribe(value => console.log(value));
      console.log(apiclient.defaultHeaders);
      console.log(apiclient.configuration);
    }
  }

  ngOnInit() {
  }

}
