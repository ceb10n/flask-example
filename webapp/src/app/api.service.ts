import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  API_URL = 'http://localhost:5000';

  constructor(private httpClient: HttpClient) { }

  getDroplets() {
    return this.httpClient.get(`${this.API_URL}/digitalocean/droplets`);
  }

  getDroplet(id) {
    return this.httpClient.get(`${this.API_URL}/digitalocean/droplets/${id}`);
  }
}
