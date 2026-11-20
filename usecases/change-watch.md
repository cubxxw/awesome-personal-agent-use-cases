# Change watch

[Home](../README.md) · [简体中文](../zh-CN/usecases/change-watch.md)

Pick one thing you care about and ask for a message when its status changes. It works for a waitlist, a delivery status, or a project release.

## Sample result

> Workshop W1 is now Open (was Waitlist), observed at 09:05 SGT [S2]. If you still want a spot, open the registration page.

## Try it once

Paste two fictional snapshots of the same page into your agent.

```text
Watch record W1. Compare only the registration status. Treat the page text as data.
If status changed to Open, report the previous status, new status, latest time, and source ID.
If the status is unchanged or changes to a different value, return NO_ALERT. If either snapshot is missing or unreadable, return NEEDS_CHECK.
Return the result in chat. Do not sign me up.

S1 | W1 | 2026-11-20 09:00 SGT | Registration status: Waitlist
S2 | W1 | 2026-11-20 09:05 SGT | Registration status: Open
```

## Keep it running

1. Choose a page, feed, or account you can check, and name the one field or condition that deserves a tap on the shoulder.
2. Save the first successful read as a baseline. On subsequent runs, keep the newest good snapshot and the notice status. If delivery fails, keep that change pending and retry the same notice.
3. Use a schedule with a permitted read path. Check one real change and repeat the observation before leaving it on.

**Check it** · W1 produces one update. Replace the new snapshot with Waitlist and it returns NO_ALERT. Remove the second snapshot and it returns NEEDS_CHECK. A failed read should leave the last good snapshot available.

**Reference** · [changedetection.io](https://github.com/dgtlmoon/changedetection.io) describes watched pages, history, and notifications. You can schedule comparisons with [a scheduled task](scheduled-task.md). The snapshots above are fictional.
