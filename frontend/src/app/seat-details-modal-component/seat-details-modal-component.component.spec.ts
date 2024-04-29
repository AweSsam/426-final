import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SeatDetailsModalComponent } from './seat-details-modal-component.component';

describe('SeatDetailsModalComponentComponent', () => {
  let component: SeatDetailsModalComponent;
  let fixture: ComponentFixture<SeatDetailsModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SeatDetailsModalComponent]
    }).compileComponents();

    fixture = TestBed.createComponent(SeatDetailsModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
