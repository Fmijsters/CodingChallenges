import {Component} from '@angular/core';
import {HomeControllerService} from '../generated/api-client';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'startup-frontend';

  constructor(private api_client: HomeControllerService) {
    api_client.getTextUsingGET().subscribe((data: String) => {
      console.log(data);
    }, error1 => console.log(error1));
  }


}
