import { TestBed } from '@angular/core/testing';

import { RoomViewService } from './room-view.service';

describe('RoomViewService', () => {
  let service: RoomViewService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RoomViewService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
