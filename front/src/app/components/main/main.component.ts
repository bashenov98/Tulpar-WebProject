import { Component, OnInit } from '@angular/core';
import { ProviderService } from 'src/app/services/provider.service';
import { Post } from '../../models/models';
@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private provider: ProviderService) { }
  posts: Post[] = [];
  ngOnInit() {
    this.provider.getPosts().then( res => {
        this.posts = res;
    });
  }

}
