package com.valorant.clip.editor.valorantclip.tests;


import java.util.concurrent.TimeUnit;

import org.drools.core.common.EventFactHandle;
import org.drools.core.time.SessionPseudoClock;
import org.junit.jupiter.api.Test;
import org.kie.api.KieServices;
import org.kie.api.runtime.KieContainer;
import org.kie.api.runtime.KieSession;

import com.valorant.clip.editor.valorantclip.model.EndRound;
import com.valorant.clip.editor.valorantclip.model.Kill;
import com.valorant.clip.editor.valorantclip.model.Round;

public class TestClass {

	@Test
	public void testShop() {
		KieServices ks = KieServices.Factory.get();
		KieContainer kieContainer = ks
				.newKieContainer(ks.newReleaseId("sbnz.integracija", "drools-valorant", "0.0.1-SNAPSHOT"));
		//KieSession kSessionPseudo = kieContainer.newKieSession("ksession-pseudo");
		KieSession kSessionRT = kieContainer.newKieSession("ksession-realtime");
		//this.runPseudoClockExample(kSessionPseudo);
		this.runRealtimeClockExample(kSessionRT);
	}

	private void runPseudoClockExample(KieSession ksession) {
		SessionPseudoClock clock = ksession.getSessionClock();
		ksession.insert(new Round());
		clock.advanceTime(10, TimeUnit.SECONDS);
		ksession.insert(new Kill());
		clock.advanceTime(20, TimeUnit.SECONDS);
		ksession.insert(new Kill());
		clock.advanceTime(20, TimeUnit.SECONDS);

		ksession.insert(new Kill());
		clock.advanceTime(20, TimeUnit.SECONDS);
		ksession.insert(new EndRound());
		int ruleCount = ksession.fireAllRules();

		System.out.println("--------------------------------------------------------------------------");

		ksession.insert(new Round());
		clock.advanceTime(10, TimeUnit.SECONDS);
		ksession.insert(new Kill());
		clock.advanceTime(20, TimeUnit.SECONDS);
		ksession.insert(new Kill());
		clock.advanceTime(20, TimeUnit.SECONDS);

		ksession.insert(new Kill());
		clock.advanceTime(20, TimeUnit.SECONDS);
		ksession.insert(new EndRound());
		ksession.fireAllRules();
	}

	private void runRealtimeClockExample(KieSession ksession) {
		Thread t = new Thread() {
			@Override
			public void run() {
				ksession.insert(new Kill(1.0));
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e1) {
					e1.printStackTrace();
				}
				EventFactHandle roundFactHandle = (EventFactHandle) ksession.insert(new Round());
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e1) {
					e1.printStackTrace();
				}
				for (int index = 0; index < 5; index++) {
					ksession.insert(new Kill(4.0 + index));
					System.out.println(roundFactHandle.getStartTimestamp());
					try {
						Thread.sleep(1000);
					} catch (InterruptedException e) {
						// do nothing
					}
				}
				ksession.insert(new EndRound());
				try {
					Thread.sleep(1000);
				} catch (InterruptedException e) {
					// do nothing
				}
				
				
			}
		};
		t.setDaemon(true);
		t.start();
		try {
			Thread.sleep(200);
		} catch (InterruptedException e) {
			// do nothing
		}
		ksession.fireUntilHalt();
	}

}
