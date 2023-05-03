import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExileComponent } from './exile.component';

describe('ExileComponent', () => {
  let component: ExileComponent;
  let fixture: ComponentFixture<ExileComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ExileComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ExileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
