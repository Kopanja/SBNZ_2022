package com.valorant.clip.editor.valorantclip.service;

import org.kie.api.runtime.KieContainer;
import org.kie.api.runtime.KieSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.valorant.clip.editor.valorantclip.model.AgentDetectedEvent;
import com.valorant.clip.editor.valorantclip.model.EndRound;
import com.valorant.clip.editor.valorantclip.model.FrameAgentDetectionEvent;
import com.valorant.clip.editor.valorantclip.model.Game;
import com.valorant.clip.editor.valorantclip.model.Kill;
import com.valorant.clip.editor.valorantclip.model.Round;



@Service
public class KieSessionService {
	private final KieSession kSession;
	private final KieContainer kieContainer;
	
	 
	@Autowired
	public KieSessionService(KieContainer kieContainer) {
		this.kieContainer = kieContainer;
		this.kSession = kieContainer.newKieSession("ksession-realtime");
		//this.kSession = kieContainer.newKieSession();
		new Thread( new Runnable() {
			  @Override
			  public void run() {
				  kSession.fireUntilHalt();
			  }
			} ).start();
			
		
	}
	
	public void insertKillEvent(Kill kill) {
		kill.setHasFrames(false);
		this.kSession.insert(kill);
	}
	
	public void insertAgentDetectedEvent(AgentDetectedEvent agentDetectedEvent) {
		this.kSession.insert(agentDetectedEvent);
	}
	
	public void insertAgentDetectedEvent(FrameAgentDetectionEvent frameAgentDetectionEvent) {
		this.kSession.insert(frameAgentDetectionEvent);
	}
	public void insertEndRound(EndRound endRound) {
		this.kSession.insert(new EndRound());
	}
	
	public void insertStartRound(Round round) {
		this.kSession.insert(new Round());
		
	}
	
	public void insertGameStart(Game game) {
		this.kSession.insert(game);
	}

}
