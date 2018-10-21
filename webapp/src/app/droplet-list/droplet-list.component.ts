import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-droplet-list',
  templateUrl: './droplet-list.component.html',
  styleUrls: ['./droplet-list.component.css']
})
export class DropletListComponent implements OnInit {

  private droplets: Array<object> = [];
  displayedColumns: string[] = ['id', 'name', 'imageName'];

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getDroplets();
  }

  public getDroplets() {
    this.apiService.getDroplets().subscribe((data: Array<object>) => {
      this.droplets = data;
    });
  }

}
