package com.valorant.clip.editor.valorantclip.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import com.valorant.clip.editor.valorantclip.model.AgentDetectedEvent;
import com.valorant.clip.editor.valorantclip.model.EndRound;
import com.valorant.clip.editor.valorantclip.model.FrameAgentDetectionEvent;
import com.valorant.clip.editor.valorantclip.model.Kill;
import com.valorant.clip.editor.valorantclip.model.Round;
import com.valorant.clip.editor.valorantclip.service.KieSessionService;


@RestController
@RequestMapping(value = "api/events")
public class EventController {
	
	@Autowired
	KieSessionService kieSessionService;
	
	
	@RequestMapping(value = "/postKill", method = RequestMethod.POST)
	public ResponseEntity<?> postKill(@RequestBody Kill killEvent) {
		kieSessionService.insertKillEvent(killEvent);
		return new ResponseEntity<String>("ok", HttpStatus.OK);
	}
	
	@RequestMapping(value = "/endRound", method = RequestMethod.POST)
	public ResponseEntity<?> postEndRound(@RequestBody EndRound endRound) {
		kieSessionService.insertEndRound(null);
		System.out.println("END");
		return new ResponseEntity<String>("ok", HttpStatus.OK);
	}
	
	@RequestMapping(value = "/buyRound", method = RequestMethod.POST)
	public ResponseEntity<?> postBuyRound(@RequestBody Round round) {
		System.out.println("AAAAAAAAAAAAAAAAAAAAAAAAAAA");
		kieSessionService.insertStartRound(null);
		
		return new ResponseEntity<String>("ok", HttpStatus.OK);
	}
	
	@RequestMapping(value = "/agentDetected", method = RequestMethod.POST)
	public ResponseEntity<?> postAgentDetection(@RequestBody AgentDetectedEvent event) {
		
		kieSessionService.insertAgentDetectedEvent(event);
		
		return new ResponseEntity<String>("ok", HttpStatus.OK);
	}
	
	
	@RequestMapping(value = "/frameAgentDetection", method = RequestMethod.POST)
	public ResponseEntity<?> postAgentDetection(@RequestBody FrameAgentDetectionEvent event) {
		
		kieSessionService.insertAgentDetectedEvent(event);
		
		return new ResponseEntity<String>("ok", HttpStatus.OK);
	}


}
