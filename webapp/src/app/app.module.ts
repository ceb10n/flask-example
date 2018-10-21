import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MatButtonModule, MatCheckboxModule, MatTableModule, MatCardModule} from '@angular/material';
import { AppComponent } from './app.component';
import { DropletListComponent } from './droplet-list/droplet-list.component';
import { DropletDetailsComponent } from './droplet-details/droplet-details.component';
import { routingModule } from './app-routing.module';

@NgModule({
  declarations: [
    AppComponent,
    DropletListComponent,
    DropletDetailsComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatCheckboxModule,
    MatTableModule,
    MatCardModule,
    routingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
