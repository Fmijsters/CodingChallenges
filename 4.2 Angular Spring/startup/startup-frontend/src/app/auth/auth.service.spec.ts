/* tslint:disable:no-unused-variable */

import {inject, TestBed} from '@angular/core/testing';
import {Router} from '@angular/router';
import {AuthService} from './auth.service';

describe('AuthService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        AuthService,
        {
          provide: Router, useValue: {
            navigate: () => {
            }
          }
        }]
    });
  });

  it('should ...', inject([AuthService], (service: AuthService) => {
    expect(service).toBeTruthy();
  }));
});
