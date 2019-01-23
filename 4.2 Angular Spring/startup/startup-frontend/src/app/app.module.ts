import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import {AppComponent} from './app.component';
import {RouterModule} from '@angular/router';
import {CallbackComponent} from './callback/callback.component';
import {HomeComponent} from './home/home.component';
import {ProfileComponent} from './profile/profile.component';
import {ROUTES} from './app.routes';
import {FormsModule} from '@angular/forms';
import {AuthGuardService} from './auth/auth-guard.service';
import {AuthService} from './auth/auth.service';

@NgModule({
  declarations: [
    AppComponent,
    CallbackComponent,
    HomeComponent,
    ProfileComponent
  ],
  imports: [
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot(ROUTES),
    BrowserModule],
  providers: [RouterModule, AuthGuardService, AuthService],
  bootstrap: [AppComponent],
  exports: [RouterModule]
})
export class AppModule {
}
