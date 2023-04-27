import { Component } from '@angular/core';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent {
 menuItems = [
    { label: 'Home', link: '/' },
    { label: 'About', link: '/about' },
    { label: 'Contact', link: '/contact' }
  ];
}
