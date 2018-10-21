import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { ActivatedRoute } from "@angular/router";
@Component({
  selector: 'app-droplet-details',
  templateUrl: './droplet-details.component.html',
  styleUrls: ['./droplet-details.component.css']
})
export class DropletDetailsComponent implements OnInit {

  private droplet: object = {};

  constructor(private route: ActivatedRoute, private apiService: ApiService) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.getDroplet(params.id);
    });
  }

  public getDroplet(id) {
    this.apiService.getDroplet(id).subscribe((data: object) => {
      this.droplet = data;
    })
  }

}
