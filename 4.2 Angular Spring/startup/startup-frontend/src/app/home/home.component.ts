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
      apiclient.getTextUsingGET().subscribe(value => console.log(value));
    }
  }2

  ngOnInit() {
  }

}
