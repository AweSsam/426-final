import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { Profile, ProfileService } from '../profile/profile.service';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent {
  public profile$: Observable<Profile | undefined>;

  public links = [
    { label: 'Enclosure and Dog Management', path: '/admin/room-view' }
  ];

  constructor(public profileService: ProfileService) {
    this.profile$ = profileService.profile$;
  }
}
