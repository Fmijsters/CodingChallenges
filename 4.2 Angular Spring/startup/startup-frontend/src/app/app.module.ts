import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {AppComponent} from './app.component';
import {RouterModule} from '@angular/router';
import {CallbackComponent} from './callback/callback.component';
import {HomeComponent} from './home/home.component';
import {ProfileComponent} from './profile/profile.component';
import {ROUTES} from './app.routes';
import {FormsModule} from '@angular/forms';
import {AuthGuardService} from './auth/auth-guard.service';
import {AuthService} from './auth/auth.service';
import {AddHeaderInterceptor} from './auth/AddHeaderIntercepter';

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
  providers: [RouterModule, AuthGuardService, AuthService, {
    provide: HTTP_INTERCEPTORS,
    useClass: AddHeaderInterceptor,
    multi: true,
  }],
  bootstrap: [AppComponent],
  exports: [RouterModule]
})
export class AppModule {
}
