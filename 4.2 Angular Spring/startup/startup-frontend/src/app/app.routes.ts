import {Routes} from '@angular/router';
import {HomeComponent} from './home/home.component';
import {CallbackComponent} from './callback/callback.component';
import {ProfileComponent} from './profile/profile.component';
import {roles} from '../config';
import {AuthGuardService as AuthGuard} from './auth/auth-guard.service';

export const ROUTES: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'callback',
    component: CallbackComponent
  },
  {
    path: 'profile',
    component: ProfileComponent,
    data: {
      roles: [roles.user]
    },
    canActivate: [AuthGuard]
  },
  {
    path: 'home',
    component: HomeComponent
  },
  {
    path: '**',
    redirectTo: ''
  }
];
