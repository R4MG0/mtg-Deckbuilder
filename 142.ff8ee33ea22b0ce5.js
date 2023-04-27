"use strict";(self.webpackChunkdeckBuilder=self.webpackChunkdeckBuilder||[]).push([[142],{142:(w,m,a)=>{a.r(m),a.d(m,{HomeModule:()=>x});var c=a(895),l=a(773),r=a(433),e=a(256),p=a(529);function u(t,i){if(1&t&&e._UZ(0,"img",5),2&t){const o=e.oxw();e.MGl("alt","Image of ",o.searchedCard.name,""),e.Q6J("src",null==o.searchedCard.image_uris?null:o.searchedCard.image_uris.png,e.LSH)}}let d=(()=>{class t{constructor(o,n){this.http=o,this.router=n,this.title="deckBuilder",this.cards=[],this.commanders=[],this.searchedCard={},this.form=new r.cw({nameOfCard:new r.NI("")})}ngOnInit(){this.http.get("https://api.magicthegathering.io/v1/cards").subscribe(o=>{this.cards.push(o)})}getCommander(){this.http.get("https://api.scryfall.com/cards/random?q=is%3Acommander").subscribe(o=>{this.commanders.push({uuid:o.id,name:o.name,cmc:o.cmc,colors:o.colors,colorIdentity:o.color_identity,image_uris:o.image_uris,keywords:o.keywords,mana_cost:o.mana_cost,power:o.power,toughness:o.toughness}),console.log(this.commanders)})}submit(){if(""===this.form.value.nameOfCard)return alert("you have to enter a card name");this.router.navigate([`home/detail/${this.form.value.nameOfCard}`])}}return t.\u0275fac=function(o){return new(o||t)(e.Y36(p.eN),e.Y36(l.F0))},t.\u0275cmp=e.Xpm({type:t,selectors:[["app-home"]],decls:7,vars:2,consts:[[1,"container"],[3,"src","alt",4,"ngIf"],[1,"search"],[3,"formGroup","submit"],["type","text","placeholder","Name of the Card","formControlName","nameOfCard",1,"inputCardName"],[3,"src","alt"]],template:function(o,n){1&o&&(e.TgZ(0,"h1"),e._uU(1,"Deck builder"),e.qZA(),e.TgZ(2,"div",0),e.YNc(3,u,1,2,"img",1),e.TgZ(4,"div",2)(5,"form",3),e.NdJ("submit",function(){return n.submit()}),e._UZ(6,"input",4),e.qZA()()()),2&o&&(e.xp6(3),e.Q6J("ngIf",null!==n.searchedCard||void 0!==n.searchedCard),e.xp6(2),e.Q6J("formGroup",n.form))},dependencies:[c.O5,r._Y,r.Fj,r.JJ,r.JL,r.sg,r.u],styles:[".container[_ngcontent-%COMP%]{background-color:#1b2845;width:100%;height:100%;display:flex;align-items:center;justify-content:center}.inputCardName[_ngcontent-%COMP%]{border:1px solid rgba(255,255,255,.25);color:#d7d7d7;background-color:transparent;padding:12px 14px 12px 54px;font-size:24px;border-radius:2px;box-shadow:0 0 2px #00000080;line-height:1.25;margin:0;width:100%;width:40em}"]}),t})(),f=(()=>{class t{constructor(o){this.http=o}getCardByName(o){const n={};return this.http.get(`https://api.scryfall.com/cards/named?fuzzy=${o}`).subscribe(s=>{n.uuid=s.id,n.name=s.name,n.cmc=s.cmc,n.colors=s.colors,n.colorIdentity=s.color_identity,n.image_uris=s.image_uris,n.keywords=s.keywords,n.mana_cost=s.mana_cost,n.power=s.power,n.toughness=s.toughness,console.log("response:",s)}),n}}return t.\u0275fac=function(o){return new(o||t)(e.LFG(p.eN))},t.\u0275prov=e.Yz7({token:t,factory:t.\u0275fac,providedIn:"root"}),t})(),g=(()=>{class t{}return t.\u0275fac=function(o){return new(o||t)},t.\u0275cmp=e.Xpm({type:t,selectors:[["app-not-found"]],decls:5,vars:0,consts:[[1,"info"],["src","http://images2.layoutsparks.com/1/160030/too-much-tv-static.gif",1,"static"]],template:function(o,n){1&o&&(e._uU(0,"br />"),e._UZ(1,"br"),e.TgZ(2,"span",0),e._uU(3,"File not found"),e.qZA(),e._UZ(4,"img",1))},styles:['@import"https://fonts.googleapis.com/css?family=Gilda+Display";html[_ngcontent-%COMP%]{background:radial-gradient(#000,#111);color:#fff;overflow:hidden;height:100%;-webkit-user-select:none;user-select:none}.static[_ngcontent-%COMP%]{width:100%;height:100%;position:relative;margin:0;padding:0;top:-100px;opacity:.05;z-index:230;-webkit-user-select:none;user-select:none;user-drag:none}.error[_ngcontent-%COMP%]{font-family:Gilda Display,serif;font-size:95px;font-style:italic;text-align:center;width:100px;height:60px;line-height:60px;margin:auto;position:absolute;inset:0 0 0 -60px;animation:_ngcontent-%COMP%_noise 2s linear infinite;overflow:default}.error[_ngcontent-%COMP%]:after{content:"404";font-family:Gilda Display,serif;font-size:100px;font-style:italic;text-align:center;width:150px;height:60px;line-height:60px;margin:auto;position:absolute;inset:0;opacity:0;color:#00f;animation:_ngcontent-%COMP%_noise-1 .2s linear infinite}.info[_ngcontent-%COMP%]{font-family:Gilda Display,serif;font-size:15px;font-style:italic;text-align:center;width:200px;height:60px;line-height:60px;margin:auto;position:absolute;inset:140px 0 0;animation:_ngcontent-%COMP%_noise-3 1s linear infinite}.error[_ngcontent-%COMP%]:before{content:"404";font-family:Gilda Display,serif;font-size:100px;font-style:italic;text-align:center;width:100px;height:60px;line-height:60px;margin:auto;position:absolute;inset:0;opacity:0;color:red;animation:_ngcontent-%COMP%_noise-2 .2s linear infinite}@keyframes _ngcontent-%COMP%_noise-1{0%,20%,40%,60%,70%,90%{opacity:0}10%{opacity:.1}50%{opacity:.5;left:-6px}80%{opacity:.3}to{opacity:.6;left:2px}}@keyframes _ngcontent-%COMP%_noise-2{0%,20%,40%,60%,70%,90%{opacity:0}10%{opacity:.1}50%{opacity:.5;left:6px}80%{opacity:.3}to{opacity:.6;left:-2px}}@keyframes _ngcontent-%COMP%_noise{0%,3%,5%,42%,44%,to{opacity:1;transform:scaleY(1)}4.3%{opacity:1;transform:scaleY(1.7)}43%{opacity:1;transform:scaleX(1.5)}}@keyframes _ngcontent-%COMP%_noise-3{0%,3%,5%,42%,44%,to{opacity:1;transform:scaleY(1)}4.3%{opacity:1;transform:scaleY(4)}43%{opacity:1;transform:scaleX(10) rotate(60deg)}}']}),t})();function h(t,i){1&t&&e._UZ(0,"app-not-found")}const y=[{path:"",component:d},{path:"detail/:cardName",component:(()=>{class t{constructor(o,n){this.route=o,this.scryfallApiService=n,this.cardName="",this.displayNotFound=!1}ngOnInit(){this.cardName=String(this.route.snapshot.paramMap.get("cardName")),this.card=this.scryfallApiService.getCardByName(this.cardName)}}return t.\u0275fac=function(o){return new(o||t)(e.Y36(l.gz),e.Y36(f))},t.\u0275cmp=e.Xpm({type:t,selectors:[["ng-component"]],decls:9,vars:7,consts:[[3,"src","alt"],[4,"ngIf"]],template:function(o,n){1&o&&(e.TgZ(0,"p"),e._uU(1,"details works!"),e.qZA(),e.TgZ(2,"h1"),e._uU(3),e.qZA(),e.TgZ(4,"pre"),e._uU(5),e.ALo(6,"json"),e.qZA(),e._UZ(7,"img",0),e.YNc(8,h,1,0,"app-not-found",1)),2&o&&(e.xp6(3),e.Oqu(n.cardName),e.xp6(2),e.Oqu(e.lcZ(6,5,n.card)),e.xp6(2),e.MGl("alt","Image of ",n.card.name,""),e.Q6J("src",null==n.card.image_uris?null:n.card.image_uris.normal,e.LSH),e.xp6(1),e.Q6J("ngIf",n.displayNotFound))},dependencies:[c.O5,g,c.Ts]}),t})()}];let C=(()=>{class t{}return t.\u0275fac=function(o){return new(o||t)},t.\u0275mod=e.oAB({type:t}),t.\u0275inj=e.cJS({imports:[l.Bz.forChild(y),l.Bz]}),t})(),_=(()=>{class t{}return t.\u0275fac=function(o){return new(o||t)},t.\u0275mod=e.oAB({type:t}),t.\u0275inj=e.cJS({imports:[c.ez]}),t})(),x=(()=>{class t{}return t.\u0275fac=function(o){return new(o||t)},t.\u0275mod=e.oAB({type:t}),t.\u0275inj=e.cJS({imports:[c.ez,C,r.UX,_]}),t})()}}]);