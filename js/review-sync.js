(function(global){"use strict";
class ReviewSync{
  constructor(options){this.base=(options.base||"").replace(/\/$/,"");this.revision=options.revision;this.sarga=options.sarga;this.onState=options.onState||function(){};this.version=0;}
  state(name,detail){this.onState(name,detail||"");}
  async request(path,options){
    if(!this.base)throw new Error("Hosted sync is not configured; local export remains available.");
    const response=await fetch(this.base+path,Object.assign({credentials:"include",headers:{"content-type":"application/json"}},options||{}));
    const body=await response.json().catch(()=>({}));
    if(!response.ok){const error=new Error(body.error||("HTTP "+response.status));error.status=response.status;error.body=body;throw error;}return body;
  }
  async save(decisions){
    if(!navigator.onLine){this.state("offline","Saved locally; remote sync will resume online.");return null;}
    this.state("syncing");
    try{const body=await this.request(`/drafts/${encodeURIComponent(this.revision)}/${this.sarga}`,{method:"PUT",body:JSON.stringify({version:this.version,decisions})});this.version=body.version;this.state("synced",`Remote draft v${body.version}`);return body;}
    catch(error){if(error.status===409){this.state("conflict","Both versions were kept; export local work before resolving.");return error.body;}this.state("error",error.message);throw error;}
  }
  async load(){const body=await this.request(`/drafts/${encodeURIComponent(this.revision)}/${this.sarga}`);this.version=body.version||0;return body;}
  async submit(payload){this.state("syncing","Creating immutable raw-submission PR…");try{const body=await this.request("/submissions",{method:"POST",body:JSON.stringify(payload)});this.state("submitted",body.content_hash||"");return body;}catch(error){this.state("error",error.message);throw error;}}
}
global.ReviewSync=ReviewSync;
})(window);
