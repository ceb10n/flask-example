import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-dropelet-list',
  templateUrl: './dropelet-list.component.html',
  styleUrls: ['./dropelet-list.component.css']
})
export class DropeletListComponent implements OnInit {

  private droplets: Array<object> = [];

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
