import {Component} from '@angular/core';
import {HomeControllerService} from '../generated/api-client';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'startup-frontend';

  constructor(private test: HomeControllerService) {
    console.log(test);
  }


}
