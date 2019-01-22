import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import {AppComponent} from './app.component';
import {RouterModule} from '@angular/router';
import {CallbackComponent} from './callback/callback.component';
import {HomeComponent} from './home/home.component';

@NgModule({
  declarations: [
    AppComponent,
    CallbackComponent,
    HomeComponent
  ],
  imports: [
    HttpClientModule,
    RouterModule.forRoot([
      {path: '', component: HomeComponent},
      {path: 'callback', component: CallbackComponent},
      {path: 'home', component: HomeComponent}
    ]),
    BrowserModule],
  providers: [RouterModule],
  bootstrap: [AppComponent],
  exports: [RouterModule]
})
export class AppModule {
}
