import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { SeatDetails } from '../room-view/room-view.models';

@Component({
  selector: 'app-seat-details-modal-component',
  templateUrl: './seat-details-modal-component.component.html',
  styleUrls: ['./seat-details-modal-component.component.css']
})
export class SeatDetailsModalComponent {
  constructor(
    @Inject(MAT_DIALOG_DATA) public data: SeatDetails,
    private dialogRef: MatDialogRef<SeatDetailsModalComponent>
  ) {}

  closeModal() {
    this.dialogRef.close();
  }
}
