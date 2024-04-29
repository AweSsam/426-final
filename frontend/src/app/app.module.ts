import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

/* HTTP and Auth */
import { RouterModule } from '@angular/router';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { HttpRequestInterceptor } from './navigation/http-request.interceptor';
import { JwtModule } from '@auth0/angular-jwt';

/* UI / Material Dependencies */
import { CommonModule, DatePipe, NgForOf } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { LayoutModule } from '@angular/cdk/layout';

/* Material UI Dependencies */
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatDialogModule } from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatIconModule } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatSliderModule } from '@angular/material/slider';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatTabsModule } from '@angular/material/tabs';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTableModule } from '@angular/material/table';
import { MatSelectModule } from '@angular/material/select';

/* Application Specific */
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavigationComponent } from './navigation/navigation.component';
import { ErrorDialogComponent } from './navigation/error-dialog/error-dialog.component';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { GateComponent } from './gate/gate.component';
import { ProfileEditorComponent } from './profile/profile-editor/profile-editor.component';
import { EventFilterPipe } from './event/event-filter/event-filter.pipe';
import { RoomViewComponent } from './room-view/room-view.component';
import { SeatDetailsModalComponent } from './seat-details-modal-component/seat-details-modal-component.component';

@NgModule({
  declarations: [
    AppComponent,
    NavigationComponent,
    ErrorDialogComponent,
    HomeComponent,
    AboutComponent,
    GateComponent,
    ProfileEditorComponent,
    RoomViewComponent,
    SeatDetailsModalComponent
  ],
  imports: [
    /* Angular */
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    AppRoutingModule,
    LayoutModule,
    ReactiveFormsModule,
    CommonModule,

    /* Material UI */
    MatButtonModule,
    MatCardModule,
    MatDialogModule,
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    MatCheckboxModule,
    MatTableModule,
    MatListModule,
    MatProgressBarModule,
    MatSidenavModule,
    MatSliderModule,
    MatSnackBarModule,
    MatTabsModule,
    MatToolbarModule,
    MatSelectModule,
    FormsModule,
    RouterModule,
    JwtModule.forRoot({
      config: {
        tokenGetter: () => {
          return localStorage.getItem('bearerToken');
        }
      }
    })
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: HttpRequestInterceptor,
      multi: true
    },
    DatePipe,
    EventFilterPipe
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
