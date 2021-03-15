/*
 * Copyright (C) 2005 - 2020 TIBCO Software Inc. All rights reserved.
 * http://www.jaspersoft.com.
 *
 * Unless you have purchased a commercial license agreement from Jaspersoft,
 * the following license terms apply:
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */

define(["require","exports","module","jquery","runtime_dependencies/js-sdk/src/common/logging/logger"],function(e,s,t){var i=e("jquery"),r=e("runtime_dependencies/js-sdk/src/common/logging/logger"),n=r.register("component-registrar"),u=function e(s){if(!this instanceof e)return new e(s);this.status="default",this.name=s,this.subscribers=[]};u.prototype={getName:function(){return this.name},getStatus:function(){return this.status},hasFinished:function(){return"finished"===this.status},subscribe:function(e){this.hasFinished()?(e.keep&&this.subscribers.push(e),this.processSubscriber(e)):this.subscribers.push(e)},trigger:function(e){var s,t=this.subscribers.length;for(s=0;s<t;s++)s-=this.processSubscriber(this.subscribers[s],e);return this.status="finished",this},reset:function(){this.status="default"},processSubscriber:function(e,s){var t,i=this.subscribers.length,r=e.args||[];if(r.push(s),e.callback.apply(e.ctx,r),!e.keep)for(t=0;t<i;t++)if(this.subscribers[t]===e)return this.subscribers.splice(t,1),1;return 0}};var c=function(e){this._events={},this.debug=e};c.prototype={subscribeToEvent:function(e){var s=this,t=this._getEventNames(e.name);i.each(t,function(t,i){s.registerEvent(i).subscribe({callback:e.callback,ctx:e.thisContext,keep:e.keep})})},registerEvent:function(e){return this._events[e]||(this._events[e]=new u(e)),this._events[e]},triggerEvent:function(e,s){this._events[e]&&(this.debug&&n.debug("triggering event: "+e),this._events[e].trigger(s))},_getEventNames:function(e){var s,t,i,r=[];if(e&&"string"==typeof e)for(s=e.split(","),t=0,i=s.length;t<i;t++)r.push(s[t].replace(/^\s+|\s+$/g,""));return r}},t.exports=c});