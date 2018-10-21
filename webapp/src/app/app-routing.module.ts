import { NgModule, ModuleWithProviders } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DropletListComponent } from './droplet-list/droplet-list.component'
import { DropletDetailsComponent } from './droplet-details/droplet-details.component'

const routes: Routes = [
  { path: '', redirectTo: 'droplets', pathMatch: 'full' },
  { path: 'droplets', component: DropletListComponent },
  { path: 'droplet/:id', component: DropletDetailsComponent }
];

export const routingModule: ModuleWithProviders = RouterModule.forRoot(routes);
